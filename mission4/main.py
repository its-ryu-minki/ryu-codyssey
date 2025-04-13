# Definition π
PI = 3.1415926535
MARS_GRAVITY_RATIO = 0.38

# Global Variable
material_result = ""
diameter_result = 0.0
thickness_result = 0.0
area_result = 0.0
weight_result = 0.0

# Calculate
def sphere_area(diameter, material='유리', thickness=1):
    global material_result, diameter_result, thickness_result, area_result, weight_result

    try:
        diameter = float(diameter)
        thickness = float(thickness)
    except ValueError:
        print("숫자를 입력해주세요.")
        return

    radius = diameter / 2
    area = 2 * PI * (radius ** 2)

    materials = {
        '유리': 2.4,
        '알루미늄': 2.7,
        '탄소강': 7.85
    }

    if material not in materials:
        print("지원하지 않는 재료입니다.")
        return

    density = materials[material]

    # Volume
    volume_cm3 = area * 10000 * thickness

    # Mass
    mass_grams = density * volume_cm3

    # Weight
    weight_kg = (mass_grams / 1000) * MARS_GRAVITY_RATIO

    # Save Result
    material_result = material
    diameter_result = round(diameter, 3)
    thickness_result = round(thickness, 3)
    area_result = round(area, 3)
    weight_result = round(weight_kg, 3)

    # Print Result
    print(f"재질 = {material_result}, 지름 = {diameter_result}m, 두께 = {thickness_result}cm, 면적 = {area_result}m², 무게 = {weight_result} kg")


# Input
d = input("돔의 지름을 입력하세요 (단위: m): ")
m = input("재질을 입력하세요 (유리 / 알루미늄 / 탄소강) [기본: 유리]: ")
t = input("두께를 입력하세요 (단위: cm) [기본: 1]: ")

# Base Value
if m.strip() == "":
    m = "유리"
if t.strip() == "":
    t = "1"

# Call
sphere_area(d, m, t)