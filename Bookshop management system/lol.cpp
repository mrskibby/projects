
//Header Files
#include <iostream>
#include <string>
#include <stdlib.h>
#include <fstream>
using namespace std;

int Login(string& admin, string& password);
int staff(string& user, string& pass1);


// node declaration
class Node {
public:
	int ID;
	string name;
	string publisherName;
	double price;	// data
	Node*	next;

	Node(int _ID, string _name, string _publisherName, double _price) {

		_ID = ID;
		_name = name;
		_publisherName = publisherName;
		_price = price;
	}	// pointer to next node
};

class queue {
public:
	Node *backPtr = NULL, *frontPtr = NULL;

	void enQueue(int _ID, string _name, string _publisherName, double _price);
	void deQueue();
	void DisplayList();
	void searchByTitle();
	//void printListByAuthor();
	//void printBookList();
	void bookManagement(int input);
};

void queue::enQueue(int _ID, string _name, string _publisherName, double _price) {

	Node *newPtr = new	Node(_ID, _name, _publisherName, _price);
	newPtr->ID = _ID;
	newPtr->name = _name;
	newPtr->price = _price;
	newPtr->publisherName = _publisherName;

	if (frontPtr == NULL) {

		newPtr->next = NULL;
		frontPtr = backPtr = newPtr;
	}

	else {

		newPtr->next = NULL;
		backPtr->next = newPtr;
		backPtr = newPtr;
	}
}

void queue::deQueue() {
	if (frontPtr == NULL) cout << "Queue is empty";
	else {
		Node *temp = frontPtr;
		frontPtr = frontPtr->next;
		temp->next = NULL;
		delete temp;
	}

}
void queue::DisplayList() {

	if (frontPtr == NULL)
		cout << "Queue is Empty" << endl;
	else
	{
			//cout<<"Book ID\t\t"<<"Book Name \t\t\t"<<"Author Name\t\t"<<"Price"<<endl;
		Node *temp = frontPtr;
		while (temp->next != NULL) {

			cout <<"Book ID: "<< temp->ID<<endl<<"Book Name: "<<temp->name<<endl<<"Author Name: "<< temp->publisherName<<endl<<"Price in RM: "<<temp->price<<endl<<endl;

			temp = temp->next;
		}

						cout <<"Book ID: "<< temp->ID<<endl<<"Book Name: "<<temp->name<<endl<<"Author Name: "<< temp->publisherName<<endl<<"Price in RM: "<<temp->price<<endl<<endl;
	}
}
void queue::searchByTitle() {
	string _title;

	cout << "Enter the title: ";
	cin >> _title;

	Node *currNode = frontPtr;
	while (currNode) {


		if (_title == currNode->name) {

					cout <<"Book ID: "<< currNode->ID<<endl<<"Book Name: "<<currNode->name<<endl<<"Author Name: "<< currNode->publisherName<<endl<<"Price: "<<currNode->price<<endl<<endl;

		}
		currNode = currNode->next;

	}

}



void queue::bookManagement(int input)
{
	int choice, x;
	int _id;
	string _name;
	string _publisherName;
	double _price;
	int _id2;
	string _name2;
	string _publisherName2;
	double _price2;



	while (1) {

		if (input == 1) {
			//Options for admins
			cout << "Select your option\n\n";
			cout << "1. Add a new book to the list\n";
			cout << "2. Remove a book from the list\n";
			cout << "3. Search for a book by Title\n";
			cout << "4. List all books\n";

			cout << "5. Back\n\n";

			do {
				cout << "Enter your choice => ";

				cin >> choice;

			} while ((choice < 1 || choice > 5) && cout << "Invalid Input!\n");

			switch (choice)
			{
			case 1:
				system("cls");
				cout<<"ID: ";
				cin>>_id;
				cout<<"name: ";
				cin>>_name;
				cout<<"Author Name: ";
				cin>>_publisherName;
				cout<<"Price in RM: ";
				cin>>_price;

				enQueue(_id,_name,_publisherName,_price);
				break;
			case 2:
				system("cls");
				deQueue();
				break;
			case 3:
				system("cls");
				searchByTitle();
				break;

			case 4:
				system("cls");
				DisplayList();
				break;

			case 5:
				return;
			}

		}

		else if (input == 2) {
			//Options for staffs
			cout << "Select your option\n\n";
			cout << "1. Add a new book to the list\n";
			cout << "2. DeQueue a book \n";
			cout << "3. Back\n\n";
			do {
				cout << "Enter your choice => ";

				cin >> choice;

			} while ((choice < 1 || choice > 3) && cout << "Invalid Input!\n");


			switch (choice)
			{
			case 1:
				system("cls");
				system("cls");
				cout<<"ID: ";
				cin>>_id2;
				cout<<"name: ";
				cin>>_name2;
				cout<<"Author Name: ";
				cin>>_publisherName2;
				cout<<"Price in RM: ";
				cin>>_price2;

				enQueue(_id2,_name2,_publisherName2,_price2);
				break;
			case 2:
				system("cls");
				deQueue();
				break;

			case 3:
				return;
			}
		}

		else if (input == 3) {
			//Options for customers
			cout << "Select your option\n\n";
			cout << "1. Search for a book by Title\n";
			cout << "2. List all books\n";
			cout << "3. Back\n\n";
			do {
				cout << "Enter your choice => ";

				cin >> choice;

			} while ((choice < 1 || choice > 3) && cout << "Invalid Input!\n");


			switch (choice)
			{
			case 1:
				system("cls");
				searchByTitle();
				break;
			case 2:
				system("cls");
				DisplayList();
				break;
			case 3:
				return;
			}
		}


		do {
			cout << "Press 1 To Show Menu Option Again: ";//For going back again
			cin >> x;

			if (x == 1)
				system("cls");

			else
				cout << "Invalid Input!\n" << endl;

		} while (x != 1);
	}
}

int main()
{

//	queue myQueue[100] ={{101," Data Structure","Dr Nor Bahiah", 26.00},{102," Computer Organization"," Dr Abd Samad ", 36.00},{103," Human Computer Interaction","Dr Sarina", 32.00},
//							{104," Database","Dr wani Zakaria", 20.00},{105," Discrete Structure"," Dr Nor Bahiah", 26.00}};
	queue myQueue ;
	myQueue.enQueue(101,"Data_Structure_and_Algorithm","Dr_Ruhaidah_Binti_Samsuddin", 26.00);
	myQueue.enQueue(102,"System_Analysis_and_Design"," Dr_Ahmad_Fadhil ", 36.00);
	myQueue.enQueue(103,"Human_Computer_Interaction","Dr_Anita_Fairos ", 32.00);
	myQueue.enQueue(104,"Database","Dr_Rozilawati_Binti_Dollah ", 20.00);
	myQueue.enQueue(105,"Network_Communication"," Dr_Johan_Bin_Sharif ", 26.00);
	myQueue.enQueue(106,"Wood_Craft"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(107,"0617898"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(108,"0176832"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(109,"0781796"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(110,"0013308"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(111,"0109153"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(112,"0901014"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(113,"0250897"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(114,"0424035"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(115,"0619201"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(116,"0753495"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(117,"0013807"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(118,"0256880"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(119,"0483623"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(120,"0630459"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(121,"0773141"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(122,"0027029"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(123,"0278120"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(124,"0501729"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(125,"0644376"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(126,"0871006"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(127,"0057882"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(128,"0292235"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(129,"0508074"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(130,"0701091"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(131,"0875372"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(132,"0076883"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(133,"0352529"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(134,"0567060"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(135,"0701307"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(136,"0893185"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(137,"0139833"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(138,"0369607"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(139,"0569165"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(140,"0708143"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(141,"0908309"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(142,"0186484"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(143,"0399925"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(144,"0578374"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(145,"0712495"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(146,"0917649"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(147,"0190730"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(148,"0418553"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(149,"0592788"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(150,"0730421"," Dr_Fabilah ", 30.00);
	myQueue.enQueue(151,"0925909"," Dr_Fabilah ", 30.00);

	int choice;
	string User;
	string password;

	do {

		system("cls");
		cin.clear();
		cout << "\n\tWelcome To RJ Bookshop Management System" << endl;
		cout << "\n******************** Please Login ***********************" << endl;
		cout << "\n\n\tPlease Select An Option From The Menu Below\n\n";
		cout << "\t\t1. Admin Login \n\n\t\t2. Staff Login \n\n\t\t3. Customer Login \n\n\t\t0. Exit";

		do {
			cout << "\n\n\tPlease Enter Your Choice : ";
			cin >> choice;
		} while (choice != 1 && choice != 2 && choice != 3 && choice != 0 && cout << "\tInvalid Input!");

		switch (choice)
		{
		case 1:
		{
			do {
				cout << "\n\tPlease Enter The Admin Username : ";
				cin >> User;
				cout << "\tPlease Enter The Password : ";
				cin >> password;

			} while (Login(User, password) == 0);

			if (Login(User, password) == 1) {

				system("cls");
				myQueue.bookManagement(choice);
				choice = 100;
			}
		}
		break;

		case 2:
		{
			do {
				cout << "\n\tPlease Enter The Staff Username : ";
				cin >> User;
				cout << "\tPlease Enter The Password : ";
				cin >> password;

			} while (staff(User, password) == 0);

			if (staff(User, password) == 1) {
				system("cls");
				myQueue.bookManagement(choice);
				choice = 100;
			}
		}
		break;

		case 3:
		{
			system("cls");
			myQueue.bookManagement(choice);
			choice = 100;
		}
		break;

		case 0:
		{
			cout << "\nApplication Successfully Closed!\n" << endl;
			system("pause");
		}

		}
	} while (choice != 0 && choice != 1 && choice != 2 && choice != 3);
}

//Admin login function
int Login(string& admin, string& password)
{
	string Users[200];
	string Pass[200];
	bool valid = false;

	int x = 0;

	ifstream UsFile;
	UsFile.open("admins.txt");

	UsFile >> Users[x] >> Pass[x];

	while (UsFile)
	{
		x++;
		if (x >= 200)
			break;

		UsFile >> Users[x] >> Pass[x];
	}

	for (int a = 0; a < x; a++)
	{
		if (admin == Users[a] && password == Pass[a])//Match the username and password with the file named admins
		{
			valid = true;
			return 1;
			break;
		}
	}

	if (!valid)
	{
		cout << "\n\tInvalid Username & Password!\t\t\n";
		return 0;
	}
}

//Staff login function
int staff(string& user, string& pass1)
{
	string Users[200];
	string Pass[200];
	bool valid = false;

	int x = 0;

	ifstream UsFile;
	UsFile.open("users.txt");

	UsFile >> Users[x] >> Pass[x];

	while (UsFile)
	{
		x++;

		if (x >= 200)
			break;

		UsFile >> Users[x] >> Pass[x];
	}

	for (int a = 0; a < x; a++)
	{
		if (user == Users[a] && pass1 == Pass[a])//Match the username and password with the file named users

		{
			valid = true;
			return 1;
			break;
		}
	}

	if (!valid)
	{
		cout << "\n\tInvalid Username & Password!\n";
		return 0;
	}
}


