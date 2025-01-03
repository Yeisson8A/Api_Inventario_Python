# Configuración del logger
import logging

logger = logging.getLogger("APIResponseLogger")
logger.setLevel(logging.DEBUG)

# Formato del logger
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# Handler para consola
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# Handler para archivo
file_handler = logging.FileHandler("app.log")
file_handler.setFormatter(formatter)

# Añadir handlers al logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)