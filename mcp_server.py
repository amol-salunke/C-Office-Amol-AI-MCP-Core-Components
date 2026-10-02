from fastmcp import FastMCP

mcp = FastMCP("Calculator Server")


@mcp.tool(
	name="add",
	description="Add two numbers and return their sum.",
	title="Add Numbers",
	tags={"calculator", "arithmetic"},
	meta={"category": "arithmetic"},
	version="1.0",
)
def add(a: float, b: float) -> float:
	"""Add two numbers and return their sum.

	Args:
		a: The first number to add.
		b: The second number to add.

	Returns:
		The sum of ``a`` and ``b``.
	"""
	return a + b


@mcp.resource(
	"training://slm/recommended-configuration",
	name="Recommended SLM Fine-tuning Configuration",
	title="Recommended SLM Fine-tuning Configuration",
	description=(
		"A practical hardware and software baseline for parameter-efficient "
		"fine-tuning of small language models."
	),
	mime_type="application/json",
	tags={"slm", "fine-tuning", "training"},
	version="1.0",
)
def get_slm_fine_tuning_configuration() -> dict[str, object]:
	"""Return a basic configuration for fine-tuning an SLM on one GPU."""
	return {
		"profile": "basic single-GPU SLM fine-tuning",
		"hardware": {
			"gpu_vram_gb": 24,
			"system_memory_gb": 32,
			"cpu_cores": 8,
			"storage": "1TB NVMe SSD",
		},
		"software": {
			"operating_system": "Ubuntu 24.04 LTS",
			"python": "3.11 or 3.12",
			"frameworks": ["PyTorch", "Transformers", "PEFT", "TRL", "bitsandbytes"],
		},
		"training": {
			"method": "4-bit QLoRA",
			"model_size": "1B-7B parameters, depending on sequence length",
			"sequence_length_tokens": 2048,
			"precision": "BF16 when supported; otherwise FP16",
			"gradient_checkpointing": True,
		},
	}


@mcp.prompt(
	name="passport_photo_image_prompt",
	title="Passport Photo Image Prompt",
	description=(
		"Create a neutral passport-style portrait prompt based on a genuine "
		"reference photo, without changing the person's identity."
	),
	tags={"photography", "passport"},
	meta={"use": "image-generation"},
	version="1.0",
)
def passport_photo_image_prompt(issuing_country: str = "unspecified") -> str:
	"""Create instructions for a truthful passport-style portrait.

	Args:
		issuing_country: Country whose official passport photo guidance should be followed.
	"""
	authority_guidance = (
		f"Follow the official photo requirements for {issuing_country}"
		if issuing_country.strip().lower() not in {"", "unspecified"}
		else "Follow the official photo requirements for the issuing country"
	)
	return (
		"Create a realistic passport-style head-and-shoulders photograph using the "
		"provided genuine reference photo. Preserve the person's identity and actual "
		"appearance; do not beautify, retouch, reshape facial features, change age, "
		"skin tone, hair, or expression, or fabricate details. Show the person facing "
		"the camera with a neutral expression, eyes visible, and mouth closed. Use a "
		"plain light background, even neutral lighting, natural color, sharp focus, "
		"and centered framing. Do not add accessories, props, text, borders, filters, "
		"or artistic effects. Follow the official photo requirements for "
		f"{authority_guidance}; do not guess dimensions or requirements if they are "
		"unknown. Passport authorities may reject AI-generated or edited images; "
		"confirm the official rules and use an unaltered genuine photo when required."
	)


if __name__ == "__main__":
	mcp.run(transport="streamable-http", host="127.0.0.1", port=8000)

