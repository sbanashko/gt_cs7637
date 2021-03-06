B
    �X�^B  �               @   s�   d Z d4dd�Zdd� Zdd� Zdd	� Zd
d� Zdd� Zdd� Zdd� Zdd� Z	dd� Z
dd� Zdd� Zdd� Zdd� Zdd� Zd5d!d"�Zd#d$� Zd6d%d&�Zd7d(d)�Zd*d+� Zd8d-d.�Zd/d0� Zd1d'lZd1d'lZd1d'lZG d2d3� d3�Zd'S )9z�
Utility functions - do not modify these functions!  Some of these functions may not be applicable to your project.  Ignore them

If you find errors post to class piazza page.

Tc             C   s4   ddl m} tttdd� t| �D �|d�|d�� �S )N�    )�
itemgetterc             S   s   g | ]\}}||f�qS � r   )�.0�i�er   r   �i/Users/urmanov/Google Drive/GATECH/SUMMER 2020/GA (CS 6515)/Coding Quizzes/CodingQuiz2/GA_ProjectUtils.py�
<listcomp>   s    z"getSortResIDXs.<locals>.<listcomp>�   )�key�reverse)�operatorr   �list�zip�sorted�	enumerate)�lZrevr   r   r   r   �getSortResIDXs   s    r   c             C   s   t | �}dd� |D �}|S )Nc             S   s   g | ]}t |�� ��qS r   )�int�strip)r   �sr   r   r   r      s    z"readIntFileDat.<locals>.<listcomp>)�readFileDat)�srcFile�strs�resr   r   r   �readIntFileDat   s    r   c             C   s   t | �}dd� |D �}|S )Nc             S   s   g | ]}t |�� ��qS r   )�floatr   )r   r   r   r   r   r       s    z$readFloatFileDat.<locals>.<listcomp>)r   )r   r   r   r   r   r   �readFloatFileDat   s    r   c          	   C   sT   dd l }yt| d�}W n( tk
r>   td�| |�� �� g S X |�� }|��  |S )Nr   �rz,Note : {} does not exist in current dir : {})�os�open�IOError�print�format�getcwd�	readlines�close)r   r   �fZ	src_linesr   r   r   r   $   s    r   c             C   s0   t | d�}x|D ]}t||d� qW |��  d S )N�w)�file)r   r!   r%   )�fNameZdatListr&   �itemr   r   r   �writeFileDat1   s    

r+   c             C   s"   t | d�}t||d� |��  d S )Nza+)r(   )r   r!   r%   )r)   �datr&   r   r   r   �appendFileDat8   s    
r-   c             C   s�   t | j�}g }xJ|D ]B}|�d�}|d �� t|d �� �t|d �� �f}|�|� qW t|dd� d�}| jdkr�td�	| j�� x*|D ]"}td	�	|d |d |d �� q�W |S )
N�,r   r	   �   c             S   s   | d S )Nr   r   )�xr   r   r   �<lambda>K   �    z(buildKnapsackItemsDict.<locals>.<lambda>)r
   zVThe following items were loaded from file {} : 
Fame, Integer Weight, Integer Value : z{0:30} Wt : {1:5} Val : {2:5} )
r   ZitemsListFileName�splitr   r   �appendr   �	autograder!   r"   )�argsZksItemsDatar   �line�valsZtupleVal�lstr   r   r   r   �buildKnapsackItemsDictC   s    


*

"r:   c             C   s�   t |�dkr�td� t|dd� d�}d}d}xB|D ]:}||d 7 }||d 7 }td�|d |d |d �� q2W td	||f � ntd
� d S )Nr   z.

Results : The following items were chosen : c             S   s   | d S )Nr   r   )r0   r   r   r   r1   Y   r2   z!displayKnapSack.<locals>.<lambda>)r
   r	   r/   z{0:30} Wt : {1:5} Val : {2:5} z4For a total value of <%i> and a total weight of [%i]z"

Results : No Items were chosen: )�lenr!   r   r"   )r6   ZitemsChosenr9   ZttlWtZttlValr   r   r   r   �displayKnapSackV   s    
"r<   c             C   sP  |d }t |�}t|�t| �kr,td� d S d}d}d}xvtt| ��D ]f}| | �� �� || �� �� krF| | �� �� }|| �� �� }	|d7 }|dkr�|d7 }qF|d7 }qFW |dkr�td� n(tdt|� d t|� d	 t|� � |d
 dk�rL|d dk�rL|d
 d t|� d t|� d t|� }
td|
 d � td|
� d S )N�valFileNamezCcompareFiles : Failure : Attempting to compare different size listsr   r	   �truez7compareResults : Your bloom filter performs as expectedzScompareResults : Number of mismatches in bloomfilter compared to validation file : z | # of incorrect true results : z!| # of incorrect False results : �studentName� r5   r/   z, zsaving results for z to autogradeResult.txtzautogradeResult.txt)r   r;   r!   �ranger   �lower�strr-   )ZresList�
configDataZbaseFileNameZbaseResZnumFailZnumFTrueResZnumFFalseResr   ZresValZ
baseResValZgradeResr   r   r   �compareResultsm   s.     

(,rE   c             C   s�  dd l }t| j�}t� }xb|D ]Z}|d dksd|kr8q|�d�}d|d krd|d �� ||d < qt|d �||d < qW d|d kr�d|d< t|t|d	 ��|d
< n�d|d k�r*d|d< g }g }|}x0|D ](}|d dkr�d|kr�|}q�|�|� q�W t|t|d	 ��|d< t|t|d	 ��|d< nd|d< t	d� t| j
�|d< |d dk�r�t|� � d �d@ |d< t	dt|d � � | j|d< | j|d< | j|d< | j|d< | j|d< t| j�|d< x6t|�� �D ]&\}	}
t	d|	 d dd � t	|
� �q�W |S )!Nr   �#�_�=�namer	   zType 1�type�kZseedszType 2r/   z	b() seeds�a�b�����z.unknown hash function specified in config fileZtaskg     @�@i���ZgenSeedzRandom Time Seed is : �
inFileName�outFileName�configFileNamer=   r?   r5   zKey = z: Val = � )�end)�timer   rQ   �dictr3   r   r   �buildSeedListr4   r!   ZtaskToDorC   rO   rP   r=   r?   r5   r   �items)r6   rT   ZbfConfigDatarD   r7   �elemsZ	aListDataZ	bListDataZlistToAppendrK   �vr   r   r   �buildBFConfigStruct�   sT    








rZ   c             C   sj   dd� t |�D �}xR| D ]J}d|ks|d dkr2q|�d�}|d �d�}t|d �|t|d �< qW |S )Nc             S   s   g | ]}d �qS )r   r   )r   r0   r   r   r   r   �   s    z!buildSeedList.<locals>.<listcomp>rG   r   rF   rH   r	   )rA   r3   r   )Z
stringListrK   r   r7   rX   ZaraElemsr   r   r   rV   �   s    

rV   c             C   sJ   | dkrdS | d dkr | d7 } x$t | | d d�D ]}t|�r2|S q2W dS )Nr/   r   r	   iP  rN   )rA   �checkIfPrime)�nr   r   r   r   �findNextPrime�   s    r]   c             C   sv   | dk rdS | dk rdS | d dks0| d dkr4dS | d }d}d}x,||krp| | dkr^dS ||7 }d	| }qFW dS )
Nr/   F�   Tr   �   g      �?�   �   r   )r\   ZsqrtNr   r'   r   r   r   r[   �   s       
 r[   c             C   s@   t | j|| j�}t|dd�\}}t||�}t|�\}}|||fS )NF)�isTest)�makeResOutFileNamerO   �sinkHandling�loadRankVectorData�buildValidationDictr   )�prObj�alpharP   ZvNodeIDs_unsrZvRankVec_unsrZ	vNodeDict�vNodeIDs�vRankVecr   r   r   �getResForPlots  s
    
rk   c             C   sD   | � � �d�}d�|d d� �}d�||dkr2dnd||d �}|S )N�.rN   z{}_{}_{}.{}r   ZSLZT3)r   r3   �joinr"   )rO   rh   rd   �nameList�
namePrefixrP   r   r   r   rc     s     rc   Fc             C   sT   | � � �d�}d�|d d� �}|r:d�|d|d �}|S d�|d|d �}|S d S )Nrl   rN   z{}-{}.{}Z
verifyRVecZoutputPR)r   r3   rm   r"   )r)   ZgetVerifyNamesrn   ro   Z	voutFName�outFNamer   r   r   �buildPROutFNames  s    rq   c       
      C   s�   ddl m} |t�}t| �}t� }xf|D ]^}|�� �d�}|d �� �d�}dd� |D �}t|d �� �}	|�|	� |�	|� |||	< q(W |t|�fS )Nr   )�defaultdict�:r	   r.   c             S   s   g | ]}t |�� ��qS r   )r   r   )r   r   r   r   r   r   ;  s    z$loadGraphADJList.<locals>.<listcomp>)
�collectionsrr   r   r   �setr   r3   r   �add�update)
r)   rr   ZresDictZfiledatZallNodesSetr7   r8   Z
adjValStrsZadjValsr
   r   r   r   �loadGraphADJList-  s    


rx   c             C   s*   t | |�}t|�}ttt|���}||fS )N)rq   r   r   rA   r;   )r)   rb   rp   �rankVecZ	rankedIDSr   r   r   re   F  s    
re   Nc             C   s,   t | �}|d kr(t||� td�|�� d S )NzRank vector saved to file {})rq   r+   r!   r"   )r)   ry   rp   r   r   r   �saveRankDataR  s    
rz   c             C   s.   i }x$t t| ��D ]}|| || | < qW |S )N)rA   r;   )ZnodeIDsry   ZvDictr0   r   r   r   rf   [  s    rf   ��h㈵��>c             C   s@  t d�| j| j| jdkrdnd�� t| jdd�\}}t| jdd�\}}t|�dks`t|�dkrlt d� dS t|�t|�kr�t d	�t|�t|��� dS t d
� t|�}t	|d �|kr�t d�|�� dS t d� t
||�}t
||�}	xLtt|��D ]<}
t	|	||
  |||
   �|kr�t d�|
||
 �� dS q�W t d� dS )NzM
Verifying results for input file "{}" using alpha={} and {} sink handling :
r   z	self loopztype 3F)rb   Tz.Validation data not found, cannot test resultsz[!!!! Error : incorrect # of nodes in calculated page rank - yours has {}; validation has {}z/Calculated Rank vector is of appropriate lengthr	   zG!!!! Error : your calculated rank vector values do not sum to 1.0 : {} z7Calculated Rank vector has appropriate magnitude of 1.0ze!!!! Error : rank vector values do not match, starting at idx {}, node {}, in validation node id listz3Rank Vector values match verification vector values)r!   r"   rO   rh   rd   re   rP   r;   �sum�absrf   rA   )rg   r6   �epsZcalcNodeIDsZcalcRankVecri   rj   ZcRVecSumZ	validDictZcalcDictr0   r   r   r   �verifyResultse  s.    $

 r   c             C   s   t d�|j| j�� d S )Nz5Running autograder on {} for prObj with input file {})r!   r"   r?   rO   )rg   r6   Z
prMadeTimer   r   r   �autogradePR�  s    r�   r   c               @   s,   e Zd Zdd� Zdd� Zdd� Zdd� Zd	S )
�findXc             C   s"   g | _ d| _d| _d| _d| _d S )Nr   )�	_findX__A�	_findX__nr0   �_findX__lookupCount�_findX__maxCalls)�selfr   r   r   �__init__�  s    zfindX.__init__c             C   sx   t �|� d| _t �dd�| _t �td�| jd �| _| j��  | jt �d| j� | _	t
t�| jd�d �d | _| j	S )Nr   i�  i'  r	   r/   r_   )�random�seedr�   �randintr�   �samplerA   r�   �sortr0   r   �math�logr�   )r�   r�   r   r   r   �start�  s    

zfindX.startc             C   s>   |  j d7  _ | j | jkr"td��|| jkr0d S | j| S d S )Nr	   z"Exceeded Maximum Number of Lookups)r�   r�   �
SystemExitr�   r�   )r�   r   r   r   r   �lookup�  s    
zfindX.lookupc             C   s   | j S )N)r�   )r�   r   r   r   �lookups�  s    zfindX.lookupsN)�__name__�
__module__�__qualname__r�   r�   r�   r�   r   r   r   r   r�   �  s   
r�   )T)F)F)N)Nr{   )�__doc__r   r   r   r   r+   r-   r:   r<   rE   rZ   rV   r]   r[   rk   rc   rq   rx   re   rz   rf   r   r�   r�   r�   �sysr�   r   r   r   r   �<module>   s4   

6


	

'