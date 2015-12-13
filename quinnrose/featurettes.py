from quinnrose.tools import Featurette

featurettes = []

# Number 1
# --------------------------------------
featurette = Featurette()
featurette.title = "Featurette #1"
featurette.sub_title = "Featurette subtitle #1"
featurette.description = 'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
featurette.image_file_name = 'featurette_01.jpg'
featurettes.append(featurette)

# Number 2
# --------------------------------------
featurette = Featurette()
featurette.title = "Featurette #2"
featurette.sub_title = "Featurette subtitle #2"
featurette.description = 'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat".'
featurette.image_file_name = 'featurette_02.jpg'
featurettes.append(featurette)

# Number 3
# --------------------------------------
featurette = Featurette()
featurette.title = "Featurette #3"
featurette.sub_title = "Featurette subtitle #3"
featurette.description = 'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft.'
featurette.image_file_name = 'featurette_03.jpg'
featurettes.append(featurette)

if __name__ == "__main__":
    print(featurettes)
    