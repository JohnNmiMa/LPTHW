import unittest
from class_def import ClassDef
class ClassDefTest(unittest.TestCase):
    def test_class_def(self):
        cd = ClassDef()
        num_inst = ClassDef.count
        self.assertEqual(1, ClassDef.count)
        cd2 = ClassDef()
        self.assertEqual(2, ClassDef.count)
        self.assertEqual(' ClassDef docstring ', cd.__doc__)

        cd.explainClassVariables()
        cd.explainInstanceFunctions()
        ClassDef.explainStaticFunctions()
        ClassDef.explainClassFunctions()
        ClassDef.explainProperties()

        print "Id of ClassDef object = {}".format(id(ClassDef))
        self.assertEqual(id(ClassDef), cd.class_id)
        print "Id of cd instance object = {}".format(id(cd))
        self.assertEqual(id(cd), cd.instance_id)
        print "Id of cd2 instance object = {}".format(id(cd2))
        self.assertNotEqual(cd.instance_id, cd2.instance_id)

        print "Calling ClassDef.class_id property is an error - requires object"
        self.assertRaises(TypeError, ClassDef.class_id)
