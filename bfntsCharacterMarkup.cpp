#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <locale>
#include <codecvt>
#include <cstdint>
#include <iterator>
#include <bitset>
#include <climits>
#include <iomanip>
using namespace std;

typedef char BYTE;
const char* filename = "./input/System.bfnt";
const char* outfilename = "./fontSystem.txt";
const int byteLine = 16;
const int startPoint = 0;

std::vector<BYTE> readAllBytes(const char* filename)
{
    std::ifstream file(filename, std::ios::binary);

    file.unsetf(std::ios::skipws);

    std::streampos fileSize;

    file.seekg(0, std::ios::end);
    fileSize = file.tellg();
    file.seekg(0, std::ios::beg);

    std::vector<BYTE> vec;
    vec.reserve(fileSize);

    vec.insert(vec.begin(),
               std::istream_iterator<BYTE>(file),
               std::istream_iterator<BYTE>());

    return vec;
}

template <typename T>
T swap_endian(T u)
{
    static_assert (CHAR_BIT == 8, "CHAR_BIT != 8");

    union
    {
        T u;
        unsigned char u8[sizeof(T)];
    } source, dest;

    source.u = u;

    for (size_t k = 0; k < sizeof(T); k++)
        dest.u8[k] = source.u8[sizeof(T) - k - 1];

    return dest.u;
}

int main()
{
	vector<BYTE> data = readAllBytes(filename);
	wchar_t character;
	bool whichTexture;
	unsigned short x;
	unsigned short y;
	int sizeX;
	int sizeY;
	int something1;
	int something2;
	ofstream outFile;
	outFile.open (outfilename, ios::out);
	for (int i = startPoint; i < data.size(); i += byteLine)
	{
		whichTexture = data[i+2] | data[i+3] << 8;
		x = data[i+5] | data[i+4] << 8;
		y = data[i+7] | data[i+6] << 8;
		sizeX = data[i+8];
		sizeY = data[i+11];
		outFile << hex << setfill('0') << setw(2) << (0xff & (unsigned int)data[i+1]);
		outFile << hex << setfill('0') << setw(2) << (0xff & (unsigned int)data[i]) << "\t";
		outFile << dec << whichTexture << "\t" << swap_endian<unsigned short>(x) << "\t" << swap_endian<unsigned short>(y) << "\t" << sizeX << "\t" << sizeY << "\t" << static_cast<int> (data[i+9]) << "\t" << static_cast<int> (data[i+11]) << endl;
	}	
	return 0;
}