#ifndef WEB2C_C_AUTO_H
#define WEB2C_C_AUTO_H

#define WEB2CVERSION " (TeX Live 2025/dev)"

#define EDITOR "vi +%d '%s'"

#define HAVE_FABS 1
#define HAVE_FMAX 1
#define HAVE_LABS 1

#ifdef _MSC_VER
#define __attribute__(A)
#endif

#define HAVE_LOCALE_H 1
#define HAVE_LONG_DOUBLE 1
#define HAVE_MKTEMP 1

#define HAVE_SETLOCALE 1
#define HAVE_STDINT_H 1
#define HAVE_STDLIB_H 1
#define HAVE_STDBOOL_H 1
#define HAVE_STRING_H 1
#define HAVE_SYS_STAT_H 1

#define IPC 1

#define RETSIGTYPE void

#define SIZEOF_INT 4
#define SIZEOF_LONG 4
#define SIZEOF_OFF_T 4

#ifdef _WIN64
#define SIZEOF_VOID_P 8
#else
#define SIZEOF_VOID_P 4
#endif

#define HAVE_UINTPTR_T 1

#endif /* !WEB2C_C_AUTO_H */
