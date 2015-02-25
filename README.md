Instructions for running the code :
	python3 perceplearn.py [trainingfile] [modelfile]
	python3 percepclassify [modelfile] < [testfile] > [outputfile]

NOTE : My implementation of perceplearn.py is based on the input and formatting of nblearn.


Part 4 :

1) Accuracy of POS tagger : 95 %

2) Precison,Recall & F-scores : 
	B-ORG : Precision: 0.8666158536585366  Recall: 0.6688235294117647 F-score: 0.75498007968

	B-MISC : Precision: 0.7201365187713311  Recall: 0.47415730337078654 F-score: 0.5718157181571816

	B-LOC : Precision: 0.7029520295202952  Recall: 0.774390243902439 F-score: 0.7369439071566731

	B-PER : Precision: 0.9245033112582781  Recall: 0.5711947626841244 F-score: 0.7061203844208398

	Overall F-score: 0.7204618345093008


3) Accuracy of Part of speech tagging using Naive Bayes classifier : 89.99 %
   
   Named entity recognition using Naive Bayes classifier :
   Overall Precision: 0.7407757805108799  Recall: 0.35991726039990807  Overall F-score : 0.500000

   The reason for the drop in accuracy of Part of speech tagger and F-score for Named entity recognition
   is because Naive Bayes assumes 'independence of words' property for a document of words. Since,part of
   speech tagging and Named entity recognition rely heavily on the context of a word , Naive Bayes doesnot
   perform well for part of speech tagging and named entity recognition.


