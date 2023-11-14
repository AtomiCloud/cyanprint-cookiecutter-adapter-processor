from cyanprintsdk.domain.core.cyan_script_model import CyanProcessorInput
from cyanprintsdk.domain.core.fs.cyan_fs_helper import CyanFileHelper
from cyanprintsdk.domain.processor.output import ProcessorOutput
from cyanprintsdk.main import start_processor_with_fn
from cookiecutter.main import cookiecutter


async def processor(i: CyanProcessorInput, fs: CyanFileHelper) -> ProcessorOutput:
    cfg = i.config

    extra_config = cfg["config"]

    if "template" in cfg and cfg["template"] != "":
        template = cfg["template"]
        cookiecutter(template, output_dir=i.write_dir, no_input=True, extra_context=extra_config)
    else:
        cookiecutter(i.read_dir, output_dir=i.write_dir, no_input=True, extra_context=extra_config)

    return ProcessorOutput(directory=i.write_dir)


start_processor_with_fn(processor)
