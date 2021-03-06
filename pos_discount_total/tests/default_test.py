import odoo.tests


@odoo.tests.common.at_install(True)
@odoo.tests.common.post_install(True)
class TestUi(odoo.tests.HttpCase):

    def test_01_pos_is_loaded_and_set_discount(self):
        self.phantom_js(
            '/web?debug=assets',

            "odoo.__DEBUG__.services['web_tour.tour']"
            ".run('pos_discount_total_tour')",

            "odoo.__DEBUG__.services['web_tour.tour']"
            ".tours.pos_discount_total_tour.ready",

            login="admin",
            timeout=240,
        )
