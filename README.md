# class6-homeworks

Load, Organize, Compute and Visualize a dataset
#************************************************

1- Filename = Get a file from input

2- List = Load dataset from the file

#Import Pandas

	2.1) Print any row of List (pandas access data by row)

	2.2) Print any column of List (pandas access data by column)

	2.3) Print any value of List(pandas access data by value)

3- Compute Mean

	N = number of all List items in each column S = sum of all List items in each column Mean = S / N

4- Compute Standard Deviation

	Sn = sum((each List item in each column - Mean) ^ 2) Std = Sqrt( Sn / (N -1)) 

#*** Second solution ***
 
#Import numpy lib

call mean() 
call std() 
 
#Import matplotlib.pyplot

5- Make the plot histogram For each column in List get values plot histogram save in a file
	 for each column in the list
		call figure method with the parameter = index of the column from matplotlib.pyplot
		call hist method by passing list columns
		call savefig to save histogram into png files

6- Make the plot scatter For each pair of columns get values plot scatter save in a file
	start from the second column (index = 1)
	while it's less than number of columns - 1 
		set j = index + 1
		while j < number of columns
			for each pairs of values in the two columns
				call scatter from matplotlib with the parameter of the values of two columns
			call savefig to save scatter into png files
			increase j by one
		increase index by one

7- Add header to the dataframe Columns = ['ID number', 'Diagnosis','Radius_M', 'Texture_M', 'Perimeter_M', 'Area_M','Smoothness_M', 'Compactness_M', 'Concavity_M', 'ConcavePoints_M', 'Symmetry_M', 'FractalDimension_M',
					  'Radius_SE', 'Texture_SE', 'Perimeter_SE', 'Area_SE','Smoothness_SE', 'Compactness_SE', 'Concavity_SE', 'ConcavePoints_SE', 'Symmetry_SE', 'FractalDimension_SE',
					  'Radius_W', 'Texture_W', 'Perimeter_W', 'Area_W','Smoothness_W', 'Compactness_W', 'Concavity_W', 'ConcavePoints_W', 'Symmetry_W', 'FractalDimension_W']

	7.1) Add attribute names with the above column names to pandas read_csv_file()
	7.2) Remove unnecessary column: 'ID number' 

8- Make a heatmap between Mean features and Diagnosis plot scatter save in a file
#Import seaborn
         for mean columns
                call heatmap method with the correlation of mean columns
		put output of get_figure() to a variable
                call savefig of that variable to save heatmap into png file



# How to run generic_parser.py:

1- Copy generic_parser.py into a path on your computer.
2- Copy BCWisconsin.csv into a path (You can copy everywhere on your computer).
3- Run generic_parser.py from 'Gitbash', 'Conda' or 'VS Code' (you need to put the csv file name and also the path in case that the file is not on the same path as python file.
4- when the script is run, the visualized files (png) will be created at the same directory as your python file.

https://towardsdatascience.com/building-a-simple-machine-learning-model-on-breast-cancer-data-eca4b3b99fa3

