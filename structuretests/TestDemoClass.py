import pytest
from structuretests.AddNumbersTest import AddNumbersClass


@pytest.mark.usefixtures("one_time_setup", "setup")
class TestDemoClass:

    @pytest.fixture(autouse=True)
    def setup_class(self,one_time_setup):
        print('The value is '+str(self.value))
        self.abc = AddNumbersClass(self.value)

    def test_add_numbers(self):
        result = self.abc.add_two_numbers(10, 10)

        assert result == 30

