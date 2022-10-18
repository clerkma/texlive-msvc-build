#define HAVE_ALLOCA 1

#define HAVE_INTTYPES_H 1

#define HAVE_LDOUBLE_IEEE_EXT_LITTLE 1

#define HAVE_LONG_LONG 1

#define HAVE_STDARG 1
#define HAVE_STDINT_H 1

#define HAVE_VA_COPY 1
#define HAVE_WCHAR_H 1

#define MPFR_HAVE_FESETROUND 1

/* gmp_printf cannot use `hh' length modifier */
#define NPRINTF_HH 1

/* gmp_printf cannot read intmax_t */
#define NPRINTF_J 1

/* gmp_printf cannot read long double */
#define NPRINTF_L 1

/* gmp_printf cannot read long long int */
#define NPRINTF_LL 1

/* gmp_printf cannot read ptrdiff_t */
#define NPRINTF_T 1

/* If using the C implementation of alloca, define if you know the
   direction of stack growth for your system; otherwise it will be
   automatically deduced at runtime.
	STACK_DIRECTION > 0 => grows toward higher addresses
	STACK_DIRECTION < 0 => grows toward lower addresses
	STACK_DIRECTION = 0 => direction of growth unknown */
/* #undef STACK_DIRECTION */

/* Define to 1 if all of the C90 standard headers exist (not just the ones
   required in a freestanding environment). This macro is provided for
   backward compatibility; new code need not use it. */
#define STDC_HEADERS 1

/* Version number of package */
//#define VERSION "4.1.0"

/* Define to `unsigned int' if <sys/types.h> does not define. */
/* #undef size_t */
