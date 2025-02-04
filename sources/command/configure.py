import logging
from typing import NoReturn
import subprocess

from globals import ExitCode, DRIVER_GENERATOR_PATH, get_driver_path
from command import boot


def execute(device: str, neg_answer_limit: int) -> NoReturn:
    """Find a driver for the infrared camera

    Args:
        device: path to the infrared camera, /dev/videoX
        neg_answer_limit: after k negative answer the pattern will be skiped. Use 256 for unlimited
    """
    logging.info("Ensure to not use the camera during the execution.")
    logging.info("Warning to do not kill the process !")

    log_level = int(logging.getLogger().level == logging.DEBUG)
    driver_path = get_driver_path(device)
    exit_code = subprocess.call([DRIVER_GENERATOR_PATH, device, str(neg_answer_limit), driver_path, str(log_level)])

    if exit_code != ExitCode.SUCCESS:
        logging.error("The configuration has failed.")
        logging.info("Do not hesitate to visit the GitHub ! https://github.com/EmixamPP/linux-enable-ir-emitter/wiki")
    else:
        logging.info("The driver has been successfully generated.")
        boot.execute("enable")

    exit(exit_code)
