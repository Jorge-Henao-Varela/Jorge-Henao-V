# --- Creación de los Conjuntos ---
# Usando el constructor set()
group_a_constructor = set(['Ana', 'Marcos', 'Carlos', 'Mario'])
print(f"Grupo A (con constructor): {group_a_constructor}")

# Usando la notación literal {}
group_b_literal = {'Ana', 'Pedro', 'Carlos', 'Antonio'}
print(f"Grupo B (literal): {group_b_literal}")
group_c_literal = {'Ana', 'Antonio', 'Marcos', 'Pepe'}
print(f"Grupo C (literal): {group_c_literal}")
group_d_literal = {'Mario', 'Pedro', 'Marcos', 'Pepe'} # Añadimos el Grupo D
print(f"Grupo D (literal): {group_d_literal}")

# --- Operaciones Básicas de Conjuntos ---

# Unión de todos los estudiantes en los grupos A, B y C
all_students_abc = group_a_constructor.union(group_b_literal, group_c_literal)
print(f"\nTodos los estudiantes en A, B o C: {all_students_abc}")

# Intersección de los grupos A y B
a_and_b_intersection = group_a_constructor.intersection(group_b_literal)
print(f"Estudiantes en A y B: {a_and_b_intersection}")

# Intersección de los grupos A y C
a_and_c_intersection = group_a_constructor.intersection(group_c_literal)
print(f"Estudiantes en A y C: {a_and_c_intersection}")

# Intersección de los grupos B y C
b_and_c_intersection = group_b_literal.intersection(group_c_literal)
print(f"Estudiantes en B y C: {b_and_c_intersection}")

# Intersección de los grupos A, B y C
common_all_abc = group_a_constructor.intersection(group_b_literal, group_c_literal)
print(f"Estudiantes en A, B y C: {common_all_abc}")

# Intersección de los cuatro grupos (A, B, C y D)
all_groups = [group_a_constructor, group_b_literal, group_c_literal, group_d_literal]
common_all_abcd = group_a_constructor.intersection(*all_groups[1:]) # Usando * para desempaquetar la lista
print(f"Estudiantes en A, B, C y D: {common_all_abcd}")

# --- Determinar el Grupo de Cada Estudiante ---

all_students_abcd = group_a_constructor.union(group_b_literal, group_c_literal, group_d_literal)

print("\n--- Grupos a los que pertenece cada estudiante ---")
groups_data = {'A': group_a_constructor, 'B': group_b_literal, 'C': group_c_literal, 'D': group_d_literal}

for student in sorted(list(all_students_abcd)): # Ordenamos para una salida más legible
    groups_in = []
    for letter, group in groups_data.items():
        if student in group:
            groups_in.append(letter)
    groups_str = '-'.join(groups_in)
    plural = 's' if len(groups_in) > 1 else ''
    print(f'{student} en grupo{plural}: {groups_str}')

# --- Métodos Disponibles para Conjuntos ---

print("\n--- Métodos Disponibles para Conjuntos ---")
print(f"Lista de métodos disponibles para conjuntos: {dir(set)}")

# Ejemplo de algunos métodos:
grupo_ejemplo = group_a_constructor.copy()
print(f"\nCopia del grupo A: {grupo_ejemplo}")
grupo_ejemplo.add('Pepe')
print(f"Copia del grupo A después de añadir 'Pepe': {grupo_ejemplo}")
grupo_ejemplo.discard('Ana')
print(f"Copia del grupo A después de descartar 'Ana': {grupo_ejemplo}")
diferencia_ab_ejemplo = group_a_constructor.difference(group_b_literal)
print(f"Diferencia entre A y B (ejemplo): {diferencia_ab_ejemplo}")
son_disjuntos_ejemplo = group_a_constructor.isdisjoint({'Luis', 'Sofia'})
print(f"¿Es A disjunto de {{'Luis', 'Sofia'}}? {son_disjuntos_ejemplo}")

# --- Álgebra de Conjuntos en Python ---

print("\n--- Álgebra de Conjuntos ---")

# Unión de A y B
union_ab = group_a_constructor.union(group_b_literal)
print(f"Unión de A y B: {union_ab}")

# Diferencia de A y B (estudiantes en A pero no en B)
difference_ab = group_a_constructor.difference(group_b_literal)
print(f"Diferencia de A y B: {difference_ab}")

# Intersección de A y B
print(f"Intersección de A y B: {group_a_constructor.intersection(group_b_literal)}")

# ¿Son A y B disjuntos?
disjoint_ab = group_a_constructor.isdisjoint(group_b_literal)
print(f"¿A y B son disjuntos? {disjoint_ab}")
print(f"¿A y un conjunto sin elementos en común son disjuntos? {group_a_constructor.isdisjoint({1, 2})}")

# ¿Es A un subconjunto de B?
subset_ab = group_a_constructor.issubset(group_b_literal)
print(f"¿Es A un subconjunto de B? {subset_ab}")
print(f"¿Es {{'Marcos'}} un subconjunto de A? {frozenset({'Marcos'}).issubset(group_a_constructor)}")
print(f"¿Es A un subconjunto de sí mismo? {group_a_constructor.issubset(group_a_constructor)}")

# ¿Es A un superconjunto de B?
superset_ab = group_a_constructor.issuperset(group_b_literal)
print(f"¿Es A un superconjunto de B? {superset_ab}")
print(f"¿Es A un superconjunto de {{'Marcos'}}? {group_a_constructor.issuperset({'Marcos'})}")
print(f"¿Es A un superconjunto de sí mismo? {group_a_constructor.issuperset(group_a_constructor)}")

# Diferencia simétrica de A y B (estudiantes que están solo en A o solo en B)
symmetric_difference_ab = group_a_constructor.symmetric_difference(group_b_literal)
print(f"Diferencia simétrica de A y B: {symmetric_difference_ab}")

# --- Otras Operaciones con Conjuntos ---

print("\n--- Otras Operaciones con Conjuntos ---")

# Longitud del grupo A
print(f"Número de estudiantes en el grupo A: {len(group_a_constructor)}")

# Añadir un estudiante al grupo A
group_a_constructor.add('Pepe')
print(f"Grupo A después de añadir a Pepe: {group_a_constructor}")

# Eliminar un estudiante del grupo A
if 'Ana' in group_a_constructor:
    group_a_constructor.remove('Ana')
    print(f"Grupo A después de eliminar a Ana: {group_a_constructor}")
else:
    print("Ana no está en el grupo A para eliminar.")

# Eliminar y devolver un estudiante arbitrario del grupo A
if group_a_constructor:
    popped_student = group_a_constructor.pop()
    print(f"Estudiante eliminado arbitrariamente de A: {popped_student}")
    print(f"Grupo A después de pop(): {group_a_constructor}")
else:
    print("El grupo A está vacío, no se puede hacer pop().")

# Eliminar un estudiante (si existe) sin generar error
group_a_constructor.discard('Ana')
print(f"Grupo A después de discard('Ana'): {group_a_constructor}")

# Comparación de conjuntos (mayor que - superconjunto propio)
print(f"¿Es el grupo A un superconjunto propio del grupo B? {group_a_constructor > group_b_literal}")

# Intentar sumar conjuntos (genera TypeError)
try:
    combined_groups = group_a_constructor + group_b_literal
except TypeError as e:
    print(f"Error al intentar sumar conjuntos: {e}")

# Operador 'or' (no es la unión de conjuntos)
print(f"Resultado de group_a_constructor or group_b_literal: {group_a_constructor or group_b_literal}")

# Operador 'and' (no es la intersección de conjuntos)
print(f"Resultado de group_a_constructor and group_b_literal: {group_a_constructor and group_b_literal}")

# Mostrar los conjuntos group_a y group_b
print(f"Grupo A: {group_a_constructor}")
print(f"Grupo B: {group_b_literal}")