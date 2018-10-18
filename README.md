# Team_ICT_Mumbai
<h2>About</h2>
<a href="http://2018.igem.org/Team:ICT-Mumbai/Software">BBrickIt</a> is a software that BioBricks any DNA sequence for you.
According to the BioBrick standards, each BioBrick part must have a Prefix and Suffix. In order for a part to be compatible with <a href="http://dspace.mit.edu/handle/1721.1/45138">BioBrick RFC 10 standards</a>, it must not contain the following restriction sites, as these are unique to the prefix and suffix:

<h3>Illegal sites</h3>
<table>
<tr>
<th>Sequence</th>
<th>Type</th>
<th>Enzyme</th>
</tr>
<tr>
<td>gaattc</td>
<td>Illegal</td>
<td>EcoRI</td>
</tr>
<tr>
<td>tctaga</td>
<td>Illegal</td>
<td>XbaI</td>
</tr>
<tr>
<td>actagt</td>
<td>Illegal</td>
<td>SpeI</td>
</tr>
<td>ctgcag</td>
<td>Illegal</td>
<td>PstI</td>
</tr>
<td>gcggccgc</td>
<td>Avoid</td>
<td>NotI</td>
</tr>
</table>

If the sequence to be contains any of these sites, the program will detect them and they will be
highlighted.
The software will also suggest another sequence, with the illegal sequences replaced by new sequences
which do not change the overall amino acid coding sequence.
The most exciting feature of this application is that it takes into account the codon preferences for your
chassis organisms. The frequency and efficiency of usage of codons in different organisms are different
for producing the same amino acid. BBrickIt takes that into account and then suggests a new sequence
that is optimized for the chassis organism.

 <h2>Steps to Use</h2>
 Follow these instructions:
 
 1. Select your Organism/Chassis.
 2. Paste your sequence in box at the top.
 3. Choose if your sequence is a coding sequence or not.
 4. Click BioBrick!
 5. If you wish to take the reverse complement of the sequence and then BioBrick it, click <Reverse Complement and BioBrick>
If your part contains any illegal restriction enzyme binding sites, two boxes will appear. The box on the left will display the highlighted restriction sites with a legend at the bottom. The box on the right will suggest the new, optimized sequence for selected organism. If you wish to proceed with that sequence, copy and paste it into top box and hit BioBrick.

Find the comprehensive user manual <a href="http://2018.igem.org/wiki/images/b/be/T--ICT-Mumbai--BBrickIt-User-Manual.pdf">here</a>.


<h2>Windows Version</h2>
Download the <a href="https://github.com/igemsoftware2018/Team_ICT_Mumbai/blob/master/BBrickIt_beta%20v1.3.1.exe">.exe file (v1.3.1)</a> and run! As simple as that.

 <h2>MAC Version</h2>
 <h4>Convert to correct file type</h4>
 Download the File <a href="https://github.com/igemsoftware2018/Team_ICT_Mumbai/blob/master/BBrickIt_India">BBrickIt_India</a>. It is a Unix Executable but appears as a text file when you download it. Follow these steps to convert it to the correct file type:
 
 1. Open terminal on your PC.
 2. Type chmod +x and a space after it.
 3. Drag your file onto the terminal window near the cursor. Your file path will automatically be copied onto the window.
 4. Press enter.
 5. You will see that your text file has been coverted to a unix executable with a change in the icon reflecting the same
 
 <h4>Give the file permission</h4>
 After you convert to the unix executable, follow these steps to get it working:
 
 1. When you attempt to open the file, the following message may pop up based on your security preferences: “BBrickIt_India” can’t be opened because it is from an unidentified developer.
 2. Go to System Preferences > Security and privacy. You will see the following message: "BBrickIt_India” was blocked from opening because it is from an unidentified developer. 
 3. Click Open Anyway.
 4. You should see the program run and display the home screen. :)
 
 The next time you click on it, it should run without any glitches!
 
 <h3>Source Code</h3>
 This progaram was coded purely using python language. Keeping in spirit with the open-source nature of creations of the iGEM community, we have made the <a href="https://github.com/igemsoftware2018/Team_ICT_Mumbai/blob/master/BBrickIt_test.py">source code</a> freely accesible to all. 
 
 
