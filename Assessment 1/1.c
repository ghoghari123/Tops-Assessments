#include <stdio.h>
#include <string.h>

void reverseString(char str[])
{
    int len = strlen(str);
    for (int i = 0; i < len / 2; i++)
    {
        char temp = str[i];
        str[i] = str[len - i - 1];
        str[len - i - 1] = temp;
    }
    printf("\nReversed String: %s\n", str);
}

void concatenateStrings(char str1[], char str2[])
{
    strcat(str1, str2);
    printf("\nConcatenated String: %s\n", str1);
}

int isPalindrome(char str[])
{
    int len = strlen(str);
    for (int i = 0; i < len / 2; i++)
    {
        if (str[i] != str[len - i - 1])
        {
            return 0; 
        }
    }
    return 1; 
}

void copyString(char str1[], char str2[])
{
    strcpy(str2, str1);
    printf("\nCopied String: %s\n", str2);
}

int stringLength(char str[])
{
    return strlen(str);
}

void characterFrequency(char str[], char ch)
{
    int count = 0;
    for (int i = 0; i < strlen(str); i++)
    {
        if (str[i] == ch)
        {
            count++;
        }
    }
    printf("\nCharacter '%c' Appears %d Times In The String.\n", ch, count);
}


void countVowelsAndConsonants(char str[])
{
    int vowels = 0, consonants = 0;
    for (int i = 0; i < strlen(str); i++)
    {
        if ((str[i] >= 'a' && str[i] <= 'z') || (str[i] >= 'A' && str[i] <= 'Z'))
        {
            if (str[i] == 'a' || str[i] == 'e' || str[i] == 'i' || str[i] == 'o' || str[i] == 'u' ||
                str[i] == 'A' || str[i] == 'E' || str[i] == 'I' || str[i] == 'O' || str[i] == 'U')
            {
                vowels++;
            }
            else
            {
                consonants++;
            }
        }
    }
    printf("\nVowels: %d, Consonants: %d\n", vowels, consonants);
}

void countSpacesAndDigits(char str[])
{
    int spaces = 0, digits = 0;
    for (int i = 0; i < strlen(str); i++)
    {
        if (str[i] == ' ')
        {
            spaces++;
        }
        else if (str[i] >= '0' && str[i] <= '9')
        {
            digits++;
        }
    }
    printf("\nBlank spaces: %d, Digits: %d\n", spaces, digits);
}

int main()
{
    char str1[200], str2[200], ch;
    int choice;

    do
    {
        
        printf("\nString Operations Menu:\n");
        printf("1. Reverse String\n");
        printf("2. Concatenate Strings\n");
        printf("3. Check Palindrome\n");
        printf("4. Copy String\n");
        printf("5. Length of String\n");
        printf("6. Character Frequency\n");
        printf("7. Count Vowels and Consonants\n");
        printf("8. Count Spaces and Digits\n");
        printf("9. Exit\n");

        
        printf("\nEnter The First String:\t");
        fgets(str1, sizeof(str1), stdin); 
        str1[strcspn(str1, "\n")] = '\0'; 

        printf("Enter Your Choice:\t");
        scanf("%d", &choice);
        getchar(); 

        switch (choice)
        {
        case 1:
            reverseString(str1);
            break;
        case 2:
            printf("Enter The Second String:\t");
            fgets(str2, sizeof(str2), stdin);
            str2[strcspn(str2, "\n")] = '\0'; 
            concatenateStrings(str1, str2);
            break;
        case 3:
            if (isPalindrome(str1))
            {
                printf("\nThe String Is A Palindrome.\n");
            }
            else
            {
                printf("\nThe String Is Not A Palindrome.\n");
            }
            break;
        case 4:
            copyString(str1, str2);
            break;
        case 5:
            printf("\nLength Of The String: %d\n", stringLength(str1));
            break;
        case 6:
            printf("Enter Character To Find Frequency: ");
            scanf("%c", &ch);
            getchar(); 
            characterFrequency(str1, ch);
            break;
        case 7:
            countVowelsAndConsonants(str1);
            break;
        case 8:
            countSpacesAndDigits(str1);
            break;
        case 9:
            printf("\nExiting The Program.\n");
            break;
        default:
            printf("\nInvalid choice. Please Try Again...!\n");
        }

        // Ask if the user wants to continue
        if (choice != 9)
        {
            printf("\nDo You Want To Continue? (y/n): ");
            scanf(" %c", &ch);
        }
    } while (ch == 'y' || ch == 'Y');

    return 0;
}