from django.test import TestCase
from .models import Employee


class EmployeeListViewTests(TestCase):
    def test_employee_list_renders_template(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'employee_list.html')

    def test_employee_pages_render_templates(self):
        employee = Employee.objects.create(
            employee_id='EMP001',
            name='Test Employee',
            email='employee@example.com',
            phone='1234567890',
            department='Engineering',
            designation='Developer',
            salary='50000.00',
            joining_date='2024-01-01',
        )
        pages = (
            ('/add/', 'employee_form.html'),
            (f'/details/{employee.pk}/', 'employee_detail.html'),
            (f'/edit/{employee.pk}/', 'employee_form.html'),
            (f'/delete/{employee.pk}/', 'employee_confirm_delete.html'),
        )

        for url, template in pages:
            with self.subTest(url=url):
                response = self.client.get(url)

                self.assertEqual(response.status_code, 200)
                self.assertTemplateUsed(response, template)
