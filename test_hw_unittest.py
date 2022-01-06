import hw
import unittest
from unittest.mock import patch

class TestFunctionsUnittest(unittest.TestCase):

    def test_add_new_doc(self):
        add_fields = {}
        add_fields['type'] = 'passpoort' # passport
        add_fields['number'] = '2207 876234' # 2207 876234
        add_fields['name'] =  'Василий Гупкин' # Василий Гупкин
        shelf = '1'
        new_documents = hw.add_to_documents(hw.documents_list, add_fields)
        if new_documents:
            self.assertDictEqual(new_documents[-1], add_fields)
            new_in_shelf = hw.add_to_shelf(hw.directories_dict, shelf, add_fields['number'])
            self.assertEqual(add_fields['number'], new_in_shelf.get(shelf)[-1])
        else:
            self.assertDictEqual(new_documents, add_fields)

    def test_find_doc(self):
        doc_number = '11-2'
        name = hw.find_doc(hw.documents_list, doc_number)
        self.assertIsNotNone(name)

    def test_find_doc_in_shelf(self):
        doc_number = '11-22'
        shelf = hw.find_doc_in_shelf(hw.directories_dict, doc_number)
        print('shelf==', shelf)
        self.assertIsNotNone(shelf)

    def test_delete_document(self):
        doc_number = '11-2'
        self.new_docs, self.new_dirs = hw.delete_document(hw.documents_list, hw.directories_dict, doc_number)

        for line in self.new_docs:
            self.assertNotEqual('Геннадий Покемонов', line.get('name'), 'found')
        for line in self.new_dirs.values():
            self.assertNotIn(doc_number, line, 'found')
 

    def test_move_document_in_shelves(self):
        mock_args = ['11-2', '3', 'y']

        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = mock_args

            for directory in hw.directories_dict.items():
                if mock_args[0] in directory[1]:
                    old_dir = directory[0]
                else:
                    old_dir = None

            moved_dir  = hw.move_document_in_shelves(hw.directories_dict)

            check_old_dir = moved_dir[old_dir]
            self.assertNotIn(mock_args[0], check_old_dir, 'It should be deleted from this shelf')

            check_new_dir = moved_dir[mock_args[1]]
            self.assertIn(mock_args[0], check_new_dir, f'Not found {mock_args[0]} in new shelf')

    @patch('builtins.input')
    def test_add_shelf(self, mock_input):
        mock_input.return_value = '6'
        add_shelf = hw.add_shelf(hw.directories_dict)
        self.assertNotIn(mock_input.return_value, add_shelf[mock_input.return_value], f'Not found new shelf') 
                    


if __name__ == '__main__':
    # a = TestFunctions()
    # a.test_add_new_doc()
    # a.test_find_doc()
    # a.test_find_doc_in_shelf()
    # a.test_delete_document()
    # a.test_move_document_in_shelves()
    # a.test_add_shelf()
    unittest.main()