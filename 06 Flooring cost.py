def main():
    area = float(input("Enter the total area of the floor (in squared meters): "))
    length, width = map(float, input("Enter the length and width of each tile (in meters): ").split())
    cost = float(input("Enter the cost of a tile (in Rupees): "))
    print(f"Your total flooring cost is: Rs {round((area*cost)/(length*width),3)}")
    
if __name__ == '__main__':
    main()