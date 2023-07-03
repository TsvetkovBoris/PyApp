import view
import model
import text


def start():
    while True:
        select = view.menu()
        match select:
            case 1:
                if model.open_file():
                    view.print_message(text.load_succesful)
                else:
                    view.print_message(text.error_load)
            case 2:
                if model.save_file():
                    view.print_message(text.save_succesful)
                else:
                    view.print_message(text.error_save)
            case 3:
                view.show_contacts(model.phones_book, text.empty_book)
            case 4:
                new = view.add_contact()
                model.add_contact(new)
                view.print_message(text.add_succesful(new.get('name')))
            case 5:
                word = view.search_word()
                result = model.search(word)
                view.show_contacts(result, text.empty_search(word))
            case 6:
                word = view.search_word()
                result = model.search(word)

                if len(result) > 0:
                    model.change(result, view.add_contact())
                else:
                    view.print_message(text.print_errors)
            case 7:
                word = view.search_word()
                result = model.search(word)
                model.delete(result)
                view.show_del(result, text.del_mess(word))
            case 8:
                view.print_message()
                break