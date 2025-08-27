from operations import operation1, operation2, operation3

def connect_all():
    """Connects all operations in sequence."""
    try:
        result1 = operation1()
        result2 = operation2(result1)
        result3 = operation3(result2)
        return result3
    except Exception as e:
        print(f"Error connecting operations: {e}")
        return None

# Example usage (assuming operation1, operation2, operation3 are defined elsewhere):
# if __name__ == "__main__":
#     final_result = connect_all()
#     print(f"Final result: {final_result}")
