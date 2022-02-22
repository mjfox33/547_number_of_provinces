from code_547_number_of_provinces import Solution

def test_example_1():
    s = Solution()
    isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    output = 2
    assert s.findCircleNum(isConnected) == output

def test_example_2():
    s = Solution()
    isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    output = 3
    assert s.findCircleNum(isConnected) == output