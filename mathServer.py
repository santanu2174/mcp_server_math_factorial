from fastmcp import FastMCP
import math

mcp = FastMCP("MathServer")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool
def factorial(a: int) -> int:
    """Calculate factorial of a number
    
    Args:
        a (int): The number to calculate the factorial of
    
    Returns:
        int: The factorial of the number
    """
    return math.factorial(a)
    

if __name__ == "__main__":
    mcp.run(transport="stdio")