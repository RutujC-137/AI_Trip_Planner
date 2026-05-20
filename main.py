from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from pydantic import BaseModel
from dotenv import load_dotenv
from agent.agentic_workflow import GraphBuilder

import os

load_dotenv()

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request Model
class QueryRequest(BaseModel):
    question: str


# Create graph only once
graph_builder = GraphBuilder(model_provider="groq")
react_app = graph_builder()


@app.get("/")
async def home():
    return {"message": "AI Travel Planner Backend Running"}


@app.post("/query")
async def query_travel_agent(query: QueryRequest):
    try:
        print("User Query:", query.question)

        # Input format
        messages = {
            "messages": [query.question]
        }

        # Invoke graph
        output = react_app.invoke(messages)

        print("RAW OUTPUT:", output)

        # Extract final answer properly
        final_output = ""

        if isinstance(output, dict):

            # Case 1
            if "messages" in output:
                msgs = output["messages"]

                if len(msgs) > 0:
                    last_msg = msgs[-1]

                    if hasattr(last_msg, "content"):
                        final_output = last_msg.content
                    else:
                        final_output = str(last_msg)

            # Case 2
            elif "message" in output:
                msgs = output["message"]

                if len(msgs) > 0:
                    last_msg = msgs[-1]

                    if hasattr(last_msg, "content"):
                        final_output = last_msg.content
                    else:
                        final_output = str(last_msg)

            else:
                final_output = str(output)

        else:
            final_output = str(output)

        return {
            "answer": final_output
        }

    except Exception as e:
        print("ERROR:", str(e))

        return JSONResponse(
            status_code=500,
            content={
                "error": str(e)
            }
        )