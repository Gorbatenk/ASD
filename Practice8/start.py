from class_generator import Generator
from practice8  import HamsterTreeBasic, HamsterTreeExtended, HamsterTreeBonus

if __name__ == "__main__":
    gen = Generator()
    hamsters = [gen.generate_single() for _ in range(5)]
    for hamster in hamsters:
        print(hamster)
    print("Basic")
    print('---')
    tree_basic = HamsterTreeBasic()
    for hamster in hamsters:
        tree_basic.insert(hamster)
    print(tree_basic)
    print('---')
    print(tree_basic.find(hamsters[0]))
    print(tree_basic.find(hamsters[1]))
    print(tree_basic.find(hamsters[2]))
    print(tree_basic.find(hamsters[3]))
    print(tree_basic.find(hamsters[4]))
    print('---')
    tree_basic.remove(hamsters[0])
    print(tree_basic)
    print('---')
    tree_basic.remove(hamsters[1])
    print(tree_basic)
    print('---')
    print("len:", len(tree_basic))
    print('---')
    print("min:", tree_basic.min())
    print('---')
    print("Extended")
    print('---')
    tree_extended = HamsterTreeExtended()
    for hamster in hamsters:
        tree_extended.insert(hamster)
    print(tree_extended)
    print('---')
    print(tree_extended.find(hamsters[0]))
    print(tree_extended.find(hamsters[1]))
    print(tree_extended.find(hamsters[2]))
    print(tree_extended.find(hamsters[3]))
    print(tree_extended.find(hamsters[4]))
    print('---')
    print("replace")
    tree_extended.replace(hamsters[0], hamsters[1])
    print(tree_extended)
    print('---')
    print("clear")
    tree_extended.clear()
    print(tree_extended)
    print('---')
    print("len:", len(tree_extended))
    print('---')
    print("extend")
    tree_extended.extend(hamsters)
    print(tree_extended)
    print('---')
    print("count")
    print(tree_extended.count(hamsters[0]))
    print(tree_extended.count(hamsters[1]))
    print(tree_extended.count(hamsters[2]))
    print(tree_extended.count(hamsters[3]))
    print(tree_extended.count(hamsters[4]))
    print('---')
    print("Bonus")
    print('---')
    tree_bonus = HamsterTreeBonus()
    for hamster in hamsters:
        tree_bonus.insert(hamster)
    print(tree_bonus)
    print('---')
    print(tree_bonus.find(hamsters[0]))
    print(tree_bonus.find(hamsters[1]))
    print(tree_bonus.find(hamsters[2]))
    print(tree_bonus.find(hamsters[3]))
    print(tree_bonus.find(hamsters[4]))
    print('---')
    print("max")
    print(tree_bonus.max())
    print('---')
    print("traversal")
    print(tree_bonus.traversal())
    print('---')
