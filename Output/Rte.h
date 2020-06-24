#ifndef RTE_H_
#define RTE_H_

typedef boolean Value_One;

typedef boolean Array_One[10];

typedef Value_One Array_Two[10];

typedef struct {
     boolean  Boolean_Element;
     Array_One  Array_Element;
     Value_One  Value_Element;
} Struct_1;

#endif