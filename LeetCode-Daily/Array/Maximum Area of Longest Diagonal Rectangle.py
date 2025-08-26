class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        diagonal = 0.0
        area = 0
        for i in range(len(dimensions)):
            dia = (((dimensions[i][0] **2) + (dimensions[i][1] ** 2)) ** 0.5)
            if dia > diagonal:
                # print(f'Dia = {dia}')
                # print(f'Diagonal = {diagonal}')
                area = (dimensions[i][0] * dimensions[i][1])
                diagonal = dia
            elif dia == diagonal:
                area = max(area,dimensions[i][0] * dimensions[i][1])
        return area
