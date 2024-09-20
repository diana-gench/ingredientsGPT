from langchain_core.prompts import PromptTemplate
from langchain.pydantic_v1 import  Field, validator
from pydantic import BaseModel
from langchain_ollama import ChatOllama
from langchain.output_parsers import  PydanticOutputParser

# Initialize the ChatOllama object
llm = ChatOllama(
    model = "llama3.1",
    temperature = 0,
)

# Define your desired data structure with improved descriptions
class Ingredient(BaseModel):
    name: str = Field(description="The name of the toothpaste ingredient being evaluated.")
    is_safe: bool = Field(description="Whether the ingredient is safe to use in toothpaste (True or False).")
    explanation: str = Field(description="A brief explanation of why the ingredient is safe or unsafe.")

    @validator("is_safe")
    def safety_must_be_boolean(cls, field):
        if not isinstance(field, bool):
            raise ValueError("Safety must be a boolean value (True or False)!")
        return field


# Set up the parser
parser = PydanticOutputParser(pydantic_object=Ingredient)

prompt_template = """You are a dental health expert tasked with evaluating the safety of toothpaste ingredients.

Instructions:
1. Evaluate the safety of the given toothpaste ingredient.
2. Determine if it's safe to use in toothpaste.
3. Provide a brief explanation for your safety assessment.

Format your response according to these instructions:
{format_instructions}

Now, please evaluate the safety of this toothpaste ingredient: {query}
"""

# Improved prompt template
prompt = PromptTemplate(
    template=prompt_template,
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

# Create the chain
chain = prompt | llm | parser
