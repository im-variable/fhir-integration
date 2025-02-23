from fastapi import FastAPI
from routers import patient, auth
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Epic FHIR API",
    description="API documentation for the Epic FHIR implementation.",
    version="2.0.0",
    contact={
        "name": "Support Team",
        "email": "support@epicfhir.com",
    },
    terms_of_service="https://fhir.epic.com/Resources/Terms",
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    }
)

app.include_router(auth.router, prefix='/oauth2', tags=['auth'])
app.include_router(patient.router, prefix='/patient', tags=['patient'])


