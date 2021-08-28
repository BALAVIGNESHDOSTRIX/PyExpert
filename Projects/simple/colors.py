# Creating the different color text

class Colors:
    Red = '\033[91m'
    Green = '\033[92m'
    Yellow = '\033[93m'
    Blue = '\033[94m'
    Cyan = '\033[96m'
    Bold = '\033[1m'
    Underline = '\033[4m'
    End = '\033[0m'


print("Color Cyan ====> ",Colors.Cyan + 'Balavignesh' + Colors.Cyan  + Colors.End + '\n')
print("Color Blue ====> ",Colors.Blue + 'Balavignesh' + Colors.Blue  + Colors.End + '\n')
print("Color Green ====> ",Colors.Green + 'Balavignesh' + Colors.Green  + Colors.End + '\n')
print("Color Yellow ====> ",Colors.Yellow + 'Balavignesh' + Colors.Yellow  + Colors.End + '\n')
print("Color Red ====> ",Colors.Red + 'Balavignesh' + Colors.Red  + Colors.End + '\n')
print("Color Bold ====> ",Colors.Bold + Colors.Yellow +'Balavignesh' + Colors.Bold  + Colors.End + '\n')
print("Color Underline ====> ",Colors.Underline + Colors.Yellow +'Balavignesh' + Colors.Underline + Colors.End + '\n')
print("Color End ====> ",Colors.End+ 'Balavignesh' + Colors.End + '\n'  )