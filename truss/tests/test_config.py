import pytest
from truss.truss_config import (
    DEFAULT_CPU,
    DEFAULT_MEMORY,
    DEFAULT_USE_GPU,
    Accelerator,
    AcceleratorSpec,
    Resources,
)


@pytest.mark.parametrize(
    "input_dict, expect_resources, output_dict",
    [
        (
            {},
            Resources(),
            {
                "cpu": DEFAULT_CPU,
                "memory": DEFAULT_MEMORY,
                "use_gpu": DEFAULT_USE_GPU,
                "accelerator": None,
            },
        ),
        (
            {"accelerator": None},
            Resources(),
            {
                "cpu": DEFAULT_CPU,
                "memory": DEFAULT_MEMORY,
                "use_gpu": DEFAULT_USE_GPU,
                "accelerator": None,
            },
        ),
        (
            {"accelerator": "V100"},
            Resources(accelerator=AcceleratorSpec(Accelerator.V100, 1), use_gpu=True),
            {
                "cpu": DEFAULT_CPU,
                "memory": DEFAULT_MEMORY,
                "use_gpu": True,
                "accelerator": "V100",
            },
        ),
        (
            {"accelerator": "T4:1"},
            Resources(accelerator=AcceleratorSpec(Accelerator.T4, 1), use_gpu=True),
            {
                "cpu": DEFAULT_CPU,
                "memory": DEFAULT_MEMORY,
                "use_gpu": True,
                "accelerator": "T4",
            },
        ),
        (
            {"accelerator": "A10G:4"},
            Resources(accelerator=AcceleratorSpec(Accelerator.A10G, 4), use_gpu=True),
            {
                "cpu": DEFAULT_CPU,
                "memory": DEFAULT_MEMORY,
                "use_gpu": True,
                "accelerator": "A10G:4",
            },
        ),
    ],
)
def test_parse_resources(input_dict, expect_resources, output_dict):
    parsed_result = Resources.from_dict(input_dict)
    assert parsed_result == expect_resources
    assert parsed_result.to_dict() == output_dict
