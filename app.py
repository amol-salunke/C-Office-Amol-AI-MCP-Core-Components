import asyncio
import json

from fastmcp import Client


async def main() -> None:
    async with Client("http://127.0.0.1:8000/mcp") as client:
        tools = await client.list_tools()

        print("Available tools:")
        for tool in tools:
            print(f"- {tool.name}")

        # Add two sample amounts using the server's calculator tool.
        result = await client.call_tool("add", {"a": 125.50, "b": 48.25})
        print(f"125.50 + 48.25 = {result.data}")

        training_configuration = await client.read_resource(
            "training://slm/recommended-configuration"
        )
        print("\nRecommended SLM fine-tuning configuration:")
        print(json.dumps(json.loads(training_configuration[0].text), indent=2))

        passport_prompt = await client.get_prompt("passport_photo_image_prompt")
        print("\nPassport photo image prompt:")
        print(passport_prompt.messages[0].content.text)


if __name__ == "__main__":
    asyncio.run(main())
    
    