class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        tuple_list = []
        for char, index in zip(s, indices):
            tuple_list.append((index, char))

        tuple_list.sort()

        answer = []
        for _, char in tuple_list:
            answer.append(char)

        return "".join(answer)
        # return "".join([ char for _, char in tuple_list])