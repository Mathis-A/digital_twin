# new deinition of the Area class using composite pattern, unfortunately, we implemented at the end
# of the project so it's not yet linked to the rest of the code

from typing import List

  
class ComponentArea:
    """
    The base ComponentArea class declares common operations for both simple and
    complex objects of a composition. A ComponentArea can be either an AtomicArea or a CompositeArea
    """


class AtomicArea(ComponentArea):
    """
    Atomic Areas represents the end objects of a composition. It can't
    have any children.


    """

    def __init__(self, name):
        '''
        We would normally define such an area with a set of walls but here we just use names to show 
        how the composite pattern works
        '''
        self.name = name
        

    def operation(self) -> str:
        return self.name


class CompositeArea(ComponentArea):
    """
    The CompositeArea represents the complex components that may have
    children. Usually, the Composite objects delegate the actual work to their
    children and then "sum-up" the result.
    """

    def __init__(self, name) -> None:
        self._children: List[ComponentArea] = []
        self.name = name

    """
    A composite object can add other components (both simple or
    complex) to its child list.
    """

    def add(self, component: ComponentArea) -> None:
        self._children.append(component)
        component.parent = self


    def operation(self) -> str:
        """
        It traverses recursively through all its children, collecting and summing
        their results. Since the composite's children pass these calls to their
        children and so forth, the whole object tree is traversed as a result.
        """

        results = []
        for child in self._children:
            results.append(child.operation())
        return f"{self.name}({'+'.join(results)})"


if __name__ == '__main__':

    entire_area = CompositeArea("entire_area")
    floor1 = CompositeArea("floor1")
    floor2 = CompositeArea("floor2")
    cafeteria = CompositeArea("cafeteria")
    A1 = AtomicArea("office1")
    A2 = AtomicArea("office2")
    A3 = AtomicArea("reception")
    A4 = AtomicArea("kitchen")
    A5 = AtomicArea("eating room")

    cafeteria.add(A4)
    cafeteria.add(A5)

    floor1.add(A3)
    floor1.add(cafeteria)

    floor2.add(A1)
    floor2.add(A2)

    entire_area.add(floor1)
    entire_area.add(floor2)

    print(entire_area.operation())

    # Output : entire_area(floor1(reception+cafeteria(kitchen+eating room))+floor2(office1+office2))
    # We describe our composite area with areas that can be as well composite ones or atomic areas using
    # recursive traversal of the composite areas.



