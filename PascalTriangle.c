#include <stdio.h>
main()
{
	int large = 0;
	
	printf("PASCAL TRIANGLE \n");
	printf("--------------------- \n");
	printf("Ingrese un valor:");
	scanf("%i", &large);
	int myValues[large][large];
	int i, value1, value2, result, j = 1;

	
	for (i = 0; i < large; i++)
	{
		for ( j = 0; j <= i; j++)
		{
			if ((i>0) && (j>0) && (j<i))
			{
				value1 = myValues[i-1][j];
				value2 = myValues[i-1][j-1];
				result = value1 + value2;
				myValues[i][j] = result;

				printf("%d-", result);
			}
			else
			{
				myValues[i][j] = 1;
				
				if (j==0)				
					printf("-%d-", 1);
				else
					printf("%d-", 1);
			}
		}
		printf("\n");	
	}

}

