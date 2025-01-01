def get_info(text: str) -> dict:
    return {"words": (words := text.split()),
            "word_count": len(words), 
            "character_count": len("".join(words))}



print(get_info("Bob"))
print(get_info("Hello, Bob"))
print(get_info("I finally get it!"))

from typing import Callable

def multiply_setup(a: float) -> Callable:
    def multiply(b: float) -> float:
        return a * b
    
    return multiply

double: Callable = multiply_setup(2)
triple: Callable = multiply_setup(3)

print(double(4))
