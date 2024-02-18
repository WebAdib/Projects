#include<bits/stdc++.h>
#include<fstream>
#include<cstdlib>
#include<ctime>
using namespace std;

int main()
{

    string ch,s,word;
    int id,r;
    srand(time(0));
    r = rand()%500;
    //cout<<r+1;

    ifstream file("D:\\WebDevelopment\\adib\\Wordle\\fiveLetterWords.txt");//D:\WebDevelopment\adib\Wordle
    if(file.is_open())
    {

        while(file>>id>>word)
        {
            if(id==r+1)
            {
                s=word;
                //cout<<s;
            }

        }
        file.close();
    }
    //cout<<"This was the word: "<<s<<endl;

    for(int i=0;i<=s.length();i++)
    {
        cout<<"Enter any 5 letter word ("<<i+1<<") : ";
        cin>>ch;
        cout<<endl;
        int count=0;
        for(int j=0;j<5;j++)
        {
            for(int k=0;k<5;k++)
            {
                if(ch[j]==s[k])
                {

                    if(j==k)
                    {
                        cout<<ch[j]<<" is in the word and in correct position\n";
                        count++;
                    }
                    else{
                        cout<<ch[j]<<" is in the word\n";
                    }

                }
            }
            //cout<<endl;
        }
        cout<<endl;
        cout<<endl;
        if(count == 5)
        {
            cout<< "---------------CONGRATULATION--------------"<<endl;
            break;
        }

    }
    cout<<"This was the word: "<<s;
    cout<<endl;
    return 0;
}

