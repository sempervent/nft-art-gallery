from fastapi import FastAPI, Request, HTTPException, Form, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from blockchain.contracts import BlockchainInterface
from models.schemas import Art

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
blockchain_interface = BlockchainInterface(
    "http://localhost:8545", "contract_address_here", "abi_here"
)


@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/gallery")
async def read_gallery(request: Request):
    arts = blockchain_interface.get_all_art()
    return templates.TemplateResponse("gallery.html", {"request": request})


@app.post("/art")
async def add_art(art: Art):
    try:
        receipt = blockchain_interface.mint_art(
            title=art.title,
            description=art.description,
            image_url=art.image_url,
            price=int(
                art.price * 1e18
            ),  # Convert Ether to Wei, assuming price is passed in Ether
        )
        return {
            "message": "Art registered successfully!",
            "transaction_receipt": receipt,
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
