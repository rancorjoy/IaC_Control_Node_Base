# _init_.py
# Routed entry point from main.py, this acts as an entry point for the repository

# Import each Python source file
from iac_control_node_base.load_config import load_config
#from iac_control_node_base.validators import validate_topology

# Run each Python source file in order
def main() -> None:
    load_config()
    #config = load_config()
    #validate_topology(config)
