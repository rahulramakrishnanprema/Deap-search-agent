from operations import operation1, operation2, operation3

def connect_all():
    """Connects all operations in sequence."""
    try:
        result1 = operation1()
        result2 = operation2(result1)
        final_result = operation3(result2)
        return final_result
    except Exception as e:
        print(f"Error connecting operations: {e}")
        return None

# Example usage (assuming operation1, operation2, operation3 are defined elsewhere):
# if __name__ == "__main__":
#     final_result = connect_all()
#     if final_result is not None:
#         print(f"Final result: {final_result}")
