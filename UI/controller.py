import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._listYear = []
        self._listCountry = []

    def fillDD(self):
        retailer = self._model._all_Retailer
        for ret in retailer:
            if ret.Country not in self._listCountry:
                self._listCountry.append(ret.Country)
        for nazione in self._listCountry:
            self._view.ddcountry.options.append(ft.dropdown.Option(f"{nazione}"))
        self._view.update_page()


    def handle_graph(self, e):
        idMap = self._model.get_IdMap()
        anno = self._view.ddyear.value
        nazione = self._view.ddcountry.value
        try:
            int_anno = int(anno)
        except ValueError:
            self._view.txt_result.controls.append(ft.Text("inserire l'anno"))
        self._model.creaGrafo(nazione,int_anno)
        self._view.update_page()


    def handle_volume(self, e):
        pass


    def handle_path(self, e):
        pass
