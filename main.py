from src.KeyFeatureDetector import KeyFeatureDetector
from src.ShapeDetector import ShapeDetector


if __name__ == "__main__":
    KFDetector = KeyFeatureDetector()
    SDetector = ShapeDetector('test.clp')

    KFDetector._read_file('shapes/segienam_beraturan.png')
    KFDetector._detect_corner()
    KFDetector._find_vertices()
    facts = KFDetector._extract_fact()

    SDetector._add_facts(facts)

    print(SDetector._detect("(segitiga_lancip_samakaki)"))

    for fact in SDetector._get_facts():
        print(fact)


    KFDetector._show_image()