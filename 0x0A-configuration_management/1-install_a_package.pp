# Description: Install Flask version 2.1.0 using pip3

# Define the package resource for Flask
package { 'Flask':
ensure   => '2.1.0',
provider => 'pip3',
}
