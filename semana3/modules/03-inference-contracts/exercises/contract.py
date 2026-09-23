from pydantic import BaseModel, Field, field_validator  # pyright: ignore[reportMissingImports]

class WineInputSchema(BaseModel):
    """
    Input schema for the wine quality prediction model.
    """
    sample_id: str = Field(..., description="Unique identifier for the wine sample")
    fixed_acidity: float = Field(..., description="Fixed acidity of the wine")
    volatile_acidity: float = Field(..., description="Volatile acidity of the wine")
    citric_acid: float = Field(..., description="Citric acid content of the wine")
    residual_sugar: float = Field(..., description="Residual sugar content of the wine")
    chlorides: float = Field(..., description="Chloride content of the wine")
    free_sulfur_dioxide: float = Field(..., description="Free sulfur dioxide content of the wine")
    total_sulfur_dioxide: float = Field(..., description="Total sulfur dioxide content of the wine")
    density: float = Field(..., description="Density of the wine")
    pH: float = Field(..., description="pH level of the wine")
    sulphates: float = Field(..., description="Sulphate content of the wine")
    alcohol: float = Field(..., description="Alcohol content of the wine")

    @field_validator('*')
    def check_positive(cls, value):
        if value < 0:
            raise ValueError("All input values must be non-negative.")
        return value