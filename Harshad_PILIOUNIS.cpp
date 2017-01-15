

#include <iostream>
using namespace std;

bool isHarshad (  int number );
int sumDigits (  int number1 );

bool isProduct (  int numbera );
int multiplyDigits (  int number2 );

int main( )
{
     int i = 1 ;
    while ( i <= 1000 )
	{
       if ( isHarshad ( i ) )
	   {
        cout << i << " " ;
		//cout << endl ;
		}
		i++ ;
		
    }
	cout << endl << endl << endl ;
	i = 10 ;
    while ( i <= 1000 )
	{
       if ( isProduct ( i ) )
	   {
        cout << i << " " ;
		//cout << endl ;
		}
		i++ ;
		
    }
      return 0 ;
}

 
bool isHarshad (  int number )
{
	 int test_num ;
    test_num = number % sumDigits ( number ) ;
	if (test_num == 0)
	{
		return true;
	}
	else
	{
		return false;
	}
}

int sumDigits (  int number1 )
 {
	 int sum = 0 ;
   while (1)
   {
        sum = sum + number1 % 10 ;
        number1 = number1 / 10;
		if (number1 == 0)
		{
			sum = sum + number1;
			break;
		}
    }
	return sum ;
}

bool isProduct (  int numbera )
{
	 int test_num ;
     int lna = multiplyDigits ( numbera );
	if (lna != 0)
	{
		test_num = numbera % lna ;
	}
	else
	{
		test_num = 1;
	}
	
	if (test_num == 0)
	{
		return true;
	}
	else
	{
		return false;
	}
}

int multiplyDigits (  int number2 )
 {
	 int prod = 1 ;
	 int locnum = 0;
   while (1)
   {
        prod = prod * (number2 % 10) ;
		locnum = number2;
        number2 = number2 / 10;
		if (number2 == 0)
		{
			 prod = prod *  locnum;
			break;
		}
    }
	
	return prod ;
}