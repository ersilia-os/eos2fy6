# Framework
# Model Modifications
Inside the framework/code folder, all the code of the original model was added. A folder named s2dv_ was created, where the original model scripts were stored. For code optimization, organization and function calls, a module s2dv_modular.py was created, which contains the functions that are called from the main.py module.In the s2dv_mainfile_original.py file the original code of the model is kept.

When carrying out reorganization of the code, redundant imports were eliminated. We made use of code that returns the probability of prediction. Functionalities that are not needed in ersilia were finally removed, such as streamlit since we don't need a web interface. The author also made some comments in Chinese which was translated to English.