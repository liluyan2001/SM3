#pragma once

#define HASH_SIZE 32 //��ϣ�����Ĵ�С

namespace SM3 {

	typedef struct sm3_context_s {

		unsigned char MessageBlock[64]; //512λ�����ݿ�

		unsigned int iv[HASH_SIZE / 4];
	}sm3_context_t;

	unsigned char* Calculate(const unsigned char* message, unsigned int messageLen, unsigned char digest[HASH_SIZE]); //���㺯��
	std::vector<uint32_t> Implement_SM3(char* filepath); //ִ��sm3

}