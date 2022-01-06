# pytest -ra 
# pytest -rfsPp

import pytest
import hw


class TestFunctionsPytest:
    
    @pytest.mark.parametrize("add_fields, shelf",[
        ({"type": "passport", "number": "2207 876234", "name": 'Василий Гупкин'}, '10'),
        ({"type": "passport", "number": "2222 245656", "name": 'Василий Гупкин'}, '10'),
        ({"type": "invoice", "number": "2222 245656", "name": 'Василий Гупкин'}, '2'),
    ])
    @pytest.mark.parametrize("documents",[
       
        [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
        ]
        
    ]) 
    def test_add_new_doc(self, add_fields, shelf, documents,  mocker):
        input_shelf = '3'
        mocker.patch('builtins.input', return_value=input_shelf)
        new_documents = hw.add_to_documents(documents, add_fields)
        if new_documents:
            assert new_documents[-1] == add_fields
            new_in_shelf = hw.add_to_shelf(hw.directories_dict, shelf, add_fields['number'])
            if new_in_shelf.get(input_shelf):
                shelf = input_shelf
            assert add_fields['number'] == new_in_shelf.get(shelf)[-1]
        else:
            assert new_documents == dict()





    @pytest.mark.parametrize("doc_number, expect_value",[
        ('11-2', 'Геннадий Покемонов'),
        ('11-2222', None),
    ])
    @pytest.mark.parametrize("documents",[
    
        [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
        ]
        
    ])
    def test_find_doc(self, doc_number, expect_value, documents):
        name = hw.find_doc(documents, doc_number)
        assert name == expect_value




    @pytest.mark.parametrize("doc_number, expect_value",[
        ('11-2', '1'),
        ('11-2222', None),
    ])  
    @pytest.mark.parametrize("directories",[
        ({
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': [] })
    ])   
    def test_find_doc_in_shelf(self, doc_number, expect_value, directories):
        shelf = hw.find_doc_in_shelf(directories, doc_number)
        assert shelf == expect_value






    @pytest.mark.parametrize("doc_number",[
        ('11-2'),
        ('11-2222'),
        ('2207 876234')
    ]) 
    @pytest.mark.parametrize("directories",[
    ({
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': [] })
    ]) 
    @pytest.mark.parametrize("documents",[
       
        [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
        ]
        
    ]) 
    def test_delete_document(self, doc_number, directories, documents):
        self.new_docs, self.new_dirs = hw.delete_document(documents, directories, doc_number)
        for line in self.new_docs:
            assert line.get('number') != doc_number
        for line in self.new_dirs.values():
            assert line != doc_number




    @pytest.mark.parametrize("doc_number, shelf, continue_adding, next_shelf, expect_answer",[
        ('11-2', '30', 'y', '2', {'1': ['2207 876234'], '2': ['10006', '11-2'], '3': []}),
        ('11-2222', '3', 'y', '3', None),
        ('2207 876234', '3', 'y', '3',  {'1': [], '2': ['10006', '11-2'], '3': ['2207 876234']})
    ])
    @pytest.mark.parametrize("directories",[
    ({
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': [] })
    ]) 
    def test_move_document_in_shelves(self, mocker, doc_number, shelf, continue_adding, next_shelf, expect_answer, directories):
        mock_args = [f'{doc_number}', f'{shelf}', f'{continue_adding}', f'{next_shelf}']
        mocker.patch('builtins.input', side_effect=mock_args)
        moved  = hw.move_document_in_shelves(directories)
        assert moved ==  expect_answer





    @pytest.mark.parametrize("directories",[
    ({
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': [] })
    ]) 
    @pytest.mark.parametrize("shelf, expect_value",[
        ('1', True),
        ('10', True),
        (None, False),
        ('', False)
    ])  
    def test_add_shelf(self, directories, shelf,  expect_value, mocker):
        mocker.patch('builtins.input', return_value=shelf)
        add_shelf = hw.add_shelf(directories).keys()
        assert (shelf in add_shelf) == expect_value