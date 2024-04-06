/* config.h for lcdf-typetools */
#ifndef __CONFIG_H__
#define __CONFIG_H__

#define HAVE_DECL_KPSE_OPENTYPE_FORMAT 1
#define HAVE_ADDRESSABLE_VA_LIST 1
#define HAVE_ADOBE_CODE 1
#define HAVE_AUTO_CFFTOT1 1
#define HAVE_AUTO_T1DOTLESSJ 1
#define HAVE_AUTO_TTFTOTYPE42 1
#define HAVE_STRERROR 1
#define HAVE_NEW_H 1
#define HAVE_INTTYPES_H 1
#define HAVE_PERMSTRING 1
#define HAVE_KPATHSEA 1

#define SIZEOF_LONG 4

#ifdef _WIN64
#define SIZEOF_VOID_P 8
#else
#define SIZEOF_VOID_P 4
#endif

#define HAVE_UINTPTR_T 1

#ifdef _MSC_VER
#include <BaseTsd.h>
typedef SSIZE_T ssize_t;
#endif

#define WORDS_BIGENDIAN 0
#define WORDS_BIGENDIAN_SET 1

#undef popen
#define popen win32_popen
#undef pclose
#define pclose win32_pclose

#ifdef __cplusplus
extern "C" {
#endif
#include <stdio.h>
extern FILE * win32_popen(const char *, const char *);
extern int win32_pclose(FILE *);
#ifdef __cplusplus
}
#endif

#define W_OK 2
#define F_OK 0
#define R_OK 4

#include <fcntl.h>

#define VERSION "2.110"
#define GLYPHLISTDIR ""
#define NOMINMAX 1 // for std::max

#ifdef PSRES 
#include <windows.h>
#endif

#define HAVE_DECL_KPSE_ENC_FORMAT 1
#define CDECL

#endif /* __CONFIG_H__ */