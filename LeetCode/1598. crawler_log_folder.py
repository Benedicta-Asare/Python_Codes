class Solution:
    def minOperations(self, logs: List[str]) -> int:
        operation = []
        for log in logs:
            if log == '../':
                if operation:
                    operation.pop()
            elif log != './':
                operation.append(log)
        return len(operation)
